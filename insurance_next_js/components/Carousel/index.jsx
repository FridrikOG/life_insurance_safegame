import React from "react";
import Image from "next/image";

const Carousel = ({ imgURL }) => {
  return (
    <div
      id="carouselExampleIndicators"
      className="carousel slide"
      data-ride="carousel"
    >
      <ol className="carousel-indicators">
        <li
          data-target="#carouselExampleIndicators"
          data-slide-to="0"
          className="active"
        ></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
      </ol>
      <div className="carousel-inner">
        <div className="carousel-item active">
          <div className="d-flex justify-content-center">
            <Image
              width={"250px"}
              height={"250px"}
              className="d-block w-100 img-carou"
              src={imgURL}
              alt="First slide"
            />
          </div>
        </div>
        <div className="carousel-item">
          <Image
            width={"250px"}
            height={"250px"}
            className="d-block w-100"
            src="/github.png"
            alt="First slide"
          />
        </div>
        <div className="carousel-item">
          <Image
            width={"250px"}
            height={"250px"}
            className="d-block w-100"
            src="/gitlab.png"
            alt="First slide"
          />
        </div>
        <a
          className="carousel-control-prev"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="prev"
        >
          <span
            className="carousel-control-prev-icon"
            aria-hidden="true"
          ></span>
          <span className="sr-only">Previous</span>
        </a>
        <a
          className="carousel-control-next"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="next"
        >
          <span
            className="carousel-control-next-icon"
            aria-hidden="true"
          ></span>
          <span className="sr-only">Next</span>
        </a>
      </div>
    </div>
  );
};

export default Carousel;
