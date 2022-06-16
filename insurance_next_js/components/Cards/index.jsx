import Link from "next/link";
import React from "react";

import Card from "./Card";

const Cards = ({ cards }) => {
  return (
    <div className="card-deck d-flex justify-content-center">
      {cards.map((c) => {
        return (
          <Link key={c.id} href="/baba">
            <Card
              key={c.id}
              imgURL={c.imgURL}
              title={c.title}
              p={c.p}
              link={c.link}
              buttonTitle={c.buttonTitle}
              pageURL={c.pageURL}
            />
          </Link>
        );
      })}
    </div>
  );
};

export default Cards;
