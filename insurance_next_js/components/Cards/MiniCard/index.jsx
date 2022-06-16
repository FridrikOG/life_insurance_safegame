import React from "react";
import Image from "next/image";

const MiniCard = ({ name, about, imgURL, color, txtColor }) => {
  return (
    <div
      className={`card ${txtColor} ${color} shadow-lg`}
      style={{ "max-width": "18rem" }}
    >
      <div className="card-header">Author</div>
      <div className="card-body">
        <div className="d-flex justify-content-center ">
          <Image
            width={"250px"}
            height={"200"}
            className="rounded-circle"
            src={imgURL}
            alt="Card image cap"
          />
        </div>

        <h5 className="card-title">{name}</h5>
        <p className="card-text">{about}</p>
      </div>
    </div>
  );
};

export default MiniCard;
