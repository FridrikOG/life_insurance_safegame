import React from "react";
import Image from "next/image";

import MiniCard from "./index";

const OrgAuthorsMiniCard = (props) => {
  return (
    <div className="card-group">
      <MiniCard
        name={"Fjölnir Þrastarson"}
        about={"flottur"}
        imgURL={"/fjolnir.png"}
        color={"bg-light"}
        txtColor={"text-black"}
      />
      <MiniCard
        name={"Friðrik Örn Gunnarsson"}
        about={"flottur"}
        imgURL={"/frikki.png"}
        color={"bg-secondary"}
        txtColor={"text-white"}
      />
      <MiniCard
        name={"Þórarinn Sigurvin Gunnarsson"}
        about={"flottur"}
        imgURL={"/toti.png"}
        color={"bg-dark"}
        txtColor={"text-white"}
      />
    </div>
  );
};

export default OrgAuthorsMiniCard;
