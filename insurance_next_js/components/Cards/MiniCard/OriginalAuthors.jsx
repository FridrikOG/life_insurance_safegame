import React from "react";
import Image from "next/image";

import MiniCard from "./index";

const OrgAuthorsMiniCard = ({ type }) => {
  return (
    <div className="card-group">
      {/* Annall */}
      {type === 1 && (
        <>
          <MiniCard
            name={"Dr. Gísli Hjálmtýsson"}
            about={
              "Dr. Gísli Hjálmtýsson is the new Dean of RU School of Computer Science."
            }
            imgURL={"/gisli.png"}
            color={"bg-light"}
            txtColor={"text-black"}
          />
          <MiniCard
            name={"Steinar Sigurðsson"}
            about={"Flottur"}
            imgURL={"/steinar.png"}
            color={"bg-dark"}
            txtColor={"text-white"}
          />
        </>
      )}

      {/* Safe Game */}
      {type === 2 && (
        <>
          <MiniCard
            name={"Dr. Gísli Hjálmtýsson"}
            about={
              "Dr. Gísli Hjálmtýsson is the new Dean of RU School of Computer Science."
            }
            imgURL={"/gisli.png"}
            color={"bg-light"}
            txtColor={"text-black"}
          />
          <MiniCard
            name={"Haraldur ehSson"}
            about={"Flottur"}
            imgURL={"/steinar.png"}
            color={"bg-dark"}
            txtColor={"text-white"}
          />
        </>
      )}
    </div>
  );
};

export default OrgAuthorsMiniCard;
