import Link from "next/link";
import React from "react";

const AboutSafeInsurance = () => {
  return (
    <div className="container d-flex justify-content-center flex-column align-items-center">
      <h1>About Insurance</h1>
      <p> empty </p>
      <div>
        <Link href="/annall">
          <button className="btn btn-dark"> Back to Annall</button>
        </Link>
      </div>
    </div>
  );
};

export default AboutSafeInsurance;
