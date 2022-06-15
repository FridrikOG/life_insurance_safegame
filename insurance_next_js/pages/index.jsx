import Head from 'next/head'

const index = () => {
  const cards = [
    {
      id: 1,
      imgURL: "/website.png",
      title: "Annall",
      p: "Website link to Annall",
      link: "https://www.annall.ru.is/",
      buttonTitle: "Website",
    },
    {
      id: 2,
      imgURL: "/documentation.png",
      title: "Documentation",
      p: "All relevant documentation can be found here.",
      link: "https://www.annall.ru.is/",
      buttonTitle: "Documentation",
    },
    {
      id: 3,
      imgURL: "/github.png",
      title: "GitHub",
      p: "Source code to the repository can be found here.",
      link: "https://github.com/pieceofGit/Annall_Lightweight_Blockchain",
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
      imgURL: "/website.png",
    },
    {
      id: 2,
      imgURL: "/documentation.png",
    },
    {
      id: 3,
      imgURL: "/gitlab.png",
    },
  ];
  return (


      <h1> here </h1>
  );
};

export default index;