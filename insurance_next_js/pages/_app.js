import Head from "next/head";
import Link from "next/link";
import Script from "next/script";
import { useEffect } from "react";

import "../styles/globals.css";

import Navbar from "../components/Navbar/Navbar";
import Footer from "../components/Footer/Footer";

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    typeof document !== undefined
      ? require("bootstrap/dist/js/bootstrap")
      : null;
  }, []);
  return (
    <>
      <Head>
        {/* Meta tag from bootstrap */}
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      {/* !! ALL BELOW NEEDED FOR NAVBAR AND BOOTSTRAP ETC !! */}
      {/* JQUERY */}
      <Script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js" />
      {/* JAVASCRIPT */}
      <Script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" />
      {/* BOOTSTRAP */}
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css"
      />

      {/* POPPER */}
      <Script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" />

      <Navbar />
      <Component {...pageProps} />
      {/* <Footer /> */}
    </>
  );
}

export default MyApp;
