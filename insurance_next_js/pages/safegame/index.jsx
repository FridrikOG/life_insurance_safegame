import React from "react";

import Cards from "../../components/Cards";
import Carousels from "../../components/Carousels";
import OrgAuthorsMiniCard from "../../components/Cards/MiniCard/OriginalAuthors";
import AddAuthorsMiniCard from "../../components/Cards/MiniCard/AdditionalAuthors";

const index = () => {
  const cards = [
    {
      id: 1,
      imgURL: "/website.png",
      title: "Safe Game",
      p: "Website link to SafeGame",
      link: "http://safegame.ru.is/",
      buttonTitle: "Website",
    },
    {
      id: 2,
      imgURL: "/documentation.png",
      title: "Documentation",
      p: "All relevant documentation can be found here regarding Safe Game.",
      link: "https://www.annall.ru.is/",
      buttonTitle: "Documentation",
    },
    {
      id: 3,
      imgURL: "/gitlab.png",
      title: "GitLab",
      p: "Source code to the repository can be found here.",
      link: "https://gitlab.com/FridrikOG/save_game",
      buttonTitle: "Repository",
    },
    {
      id: 4,
      imgURL: "/presentation.png",
      title: "Presentation",
      p: "Presentation of Annall.",
      link: "https://www.canva.com/design/DAFC9fG4WmM/EYkK-N9sl3H-xVUQXfXa3A/edit?utm_content=DAFC9fG4WmM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton",
      buttonTitle: "Slides",
    },
    {
      id: 5,
      imgURL: "/info.png",
      title: "About",
      p: "Lightweight-Component based blockchain.",
      link: "/about/annall",
      buttonTitle: "More details",
    },
  ];
  const carousels = [
    {
      id: 1,
      imgURL: "/safegame1.png",
    },
    {
      id: 2,
      imgURL: "/safegame2.png",
    },
    {
      id: 3,
      imgURL: "/safegame3.png",
    },
    {
      id: 4,
      imgURL: "/safegame4.png",
    },
    {
      id: 5,
      imgURL: "/safegame5.png",
    },
    {
      id: 6,
      imgURL: "/safegame6.png",
    },
    {
      id: 7,
      imgURL: "/safegame5.png",
    },
    {
      id: 8,
      imgURL: "/safegame5.png",
    },
    {
      id: 9,
      imgURL: "/safegame5.png",
    },
  ];
  return (
    <div className="container">
      <br />
      <br />
      <h1 className="d-flex justify-content-center text-dark">Safe Game</h1>
      <br />
      <br />
      {/* <Introduction /> */}

      {/* Card1 */}
      <div className="d-flex justify-content-center">
        <Cards cards={cards} />
      </div>

      <br />
      <br />
      <br />
      <br />
      <h1 className="d-flex justify-content-center text-dark">Images</h1>
      <div className="rounded caro-bg shadow-lg">
        <Carousels carousels={carousels} />
      </div>

      <br />
      <br />
      <br />
      <br />

      <h1 className="d-flex justify-content-center text-dark">
        Original Authors
      </h1>
      <div className="d-flex card-deck justify-content-center bg-secondary shadow-lg rounded m-5 p-3">
        <OrgAuthorsMiniCard type={2} />
      </div>

      <br />
      <br />
      <br />
      <br />

      <h1 className="d-flex justify-content-center text-dark">
        Additional Authors
      </h1>
      <div className="d-flex card-deck justify-content-center bg-dark.bg-gradient shadow-lg rounded m-5 p-3">
        <AddAuthorsMiniCard />
      </div>

      <br />
      <br />
      <br />
      <br />
    </div>
  );
};

export default index;
