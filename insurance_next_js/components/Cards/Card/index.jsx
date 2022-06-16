import React from "react";
import Image from "next/image";

import cardStyles from "../../../styles/Card.module.css";
import Link from "next/link";

const Card = ({ imgURL, title, p, link, buttonTitle }) => {
  return (
    <Link href={link}>
      <div
        className={`card shadow-lg ${cardStyles.cardBg} mb-3`}
        style={{ minWidth: "18rem", maxWidth: "18rem" }}
      >
        <div className={`${cardStyles.top} d-flex justify-content-center`}>
          <Image
            width={"250px"}
            height={"250px"}
            className="card-img-top p-4 rounded-circle"
            src={imgURL}
            alt="Card image cap"
          />
        </div>
        <div className="card-body d-flex flex-column justify-content-center align-items-center">
          <div>
            <span className="badge badge-dark">code</span>
            <span className="badge badge-success">{title}</span>
            <span className="badge badge-info">research</span>
          </div>
          <h2 className="card-title ">{title}</h2>
          <p className="card-text">{p}</p>
          <a href={link} className="btn btn-secondary mt-auto">
            {buttonTitle}
          </a>
          <p className="card-text">
            <small className="text-muted">Last updated 2022 </small>
          </p>
        </div>
      </div>
    </Link>
  );
};

export default Card;
