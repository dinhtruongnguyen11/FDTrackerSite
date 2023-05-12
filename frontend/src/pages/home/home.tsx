import Head from "next/head";
import styles from "@/styles/Home.module.css";
import { GetServerSideProps } from "next";
import axios from "axios";
import HomeContext from "./home.context";
import { useCreateReducer } from "../../../hooks/useCreateReducer";
import { HomeInitialState, initialState } from "./home.state";

export default function Home() {
  const contextValue = useCreateReducer<HomeInitialState>({
    initialState,
  });

  return (
    <>
      <HomeContext.Provider value={{ ...contextValue }}>
        <Head>
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <main className={styles.main}></main>
      </HomeContext.Provider>
    </>
  );
}

export const getServerSideProps: GetServerSideProps = async () => {
  const { data } = await axios.get("http://127.0.0.1:8000/filter");
  console.log(data);
  return {
    props: {},
  };
};
