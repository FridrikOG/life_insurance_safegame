import React from "react";
import Link from "next/link";
import Image from "next/image";

const Navbar = () => {
  return (
    <>
      <nav className="navbar  navbar-expand-lg navbar-dark bg-dark shadow-lg ">
        <div className="navbar-brand m-1">
          <Link href="/">
            <h1>The Annall Project</h1>
          </Link>
        </div>

        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navCollapse"
          aria-controls="navCollapse"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navCollapse">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <div className="nav-link">
                <Link href="/">Home</Link>
              </div>
            </li>
            <li className="nav-item">
              <div className="nav-link">
                <Link href="/annall">Annall</Link>
              </div>
            </li>
            <li className="nav-item">
              <div className="nav-link">
                <Link href="/safegame">SafeGame</Link>
              </div>
            </li>
          </ul>
          <div>
            <Image
              width={"200"}
              height={"200px"}
              src="/ru-banner.svg"
              alt="RU image"
              // className="rounded w-100 m-4"
            />
            <span className="navbar-text">
              Property of University of Reykjavik
            </span>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
