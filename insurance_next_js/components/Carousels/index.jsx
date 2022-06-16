import React from "react";
import Image from "next/image";

import Carousel from "../../components/Carousel";

const index = ({ carousels }) => {
  return (
    <div
      id="carouselExampleIndicators"
      className="carousel slide"
      data-ride="carousel"
    >
      <ol className="carousel-indicators">
        {carousels.map((c) => {
          return c.id === 1 ? (
            <li
              data-target="#carouselExampleIndicators"
              data-slide-to={c.id}
              className="active"
            ></li>
          ) : (
            <li
              data-target="#carouselExampleIndicators"
              data-slide-to={c.id}
            ></li>
          );
        })}
      </ol>

      <div className="carousel-inner">
        {carousels.map((c) => {
          return c.id === 1 ? (
            // ACTIVE
            <div key={c.id} className="carousel-item active">
              <div key={c.id} className="d-flex justify-content-center">
                <Image
                  key={c.id}
                  width={"1920"}
                  height={"1080px"}
                  className="d-block w-100 rounded"
                  src={c.imgURL}
                  alt="First slide"
                />
              </div>
            </div>
          ) : (
            // NOT ACTIVE
            <div key={c.id} className="carousel-item">
              <div key={c.id} className="d-flex justify-content-center">
                <Image
                  key={c.id}
                  width={"1920px"}
                  height={"1080px"}
                  className="d-block w-100 rounded"
                  src={c.imgURL}
                  alt="First slide"
                />
              </div>
            </div>
          );
        })}
      </div>
      <a
        className="carousel-control-prev"
        href="#carouselExampleIndicators"
        role="button"
        data-slide="prev"
      >
        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
        <span className="sr-only">Previous</span>
      </a>
      <a
        className="carousel-control-next"
        href="#carouselExampleIndicators"
        role="button"
        data-slide="next"
      >
        <span className="carousel-control-next-icon" aria-hidden="true"></span>
        <span className="sr-only">Next</span>
      </a>
    </div>
  );
};

export default index;
