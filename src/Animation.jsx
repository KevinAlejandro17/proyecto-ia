import React, { useRef, useEffect, useState, useCallback } from "react";
import { fetchData } from "./Utils";
import { useStore } from "./useStore";
import { Matrix } from "./components/Matrix";


const CELL_SIZE = 40;
const CELL_VALUES = {
  0: "#FFF",
  1: "#777",
  2: "#FFF",
  3: "#FFF",
  4: "#FFF",
  5: "#FFF",
};

const initialMatrix = [
  [0, 0, 0, 0, 0, 1, 1, 0, 0, 5],
  [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
  [0, 1, 0, 0, 4, 4, 4, 0, 1, 0],
  [2, 0, 0, 1, 1, 1, 0, 1, 1, 0],
  [0, 1, 0, 4, 4, 0, 0, 1, 1, 0],
  [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
  [0, 0, 0, 0, 1, 1, 0, 0, 3, 0],
  [1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
  [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
];

const PathAnimation = () => {
  const canvasRef = useRef(null);
  const [response, setResponse] = useState({});
  const { algoritmoActual } = useStore();

  const path = response?.path;
  const delay = 200;
  const stepRef = useRef(0);
  const animationRef = useRef(null);
  const isMounted = useRef(false);

  const handleButtonClick = () => {
    stopAnimation();
    fetchData(algoritmoActual.id)
    .then((data) => setResponse(data));
  };

  useEffect(() => {
    if (algoritmoActual && algoritmoActual.id) {
      const fetchDataAndStartAnimation = async () => {
        const data = await fetchData(algoritmoActual?.id);
        setResponse(data);
      /*   setTimeout(() => {
          if (isMounted.current) {
            animationRef.current = requestAnimationFrame(drawPath);
          }
        }, 1000); // Esperar 1 segundo antes de iniciar la animación */
      };
      fetchDataAndStartAnimation();
    }
  }, [algoritmoActual]);

  useEffect(() => {
    path && console.log(path)
  }, [path])
  
 
  return (
    <>
      <h4 className="text-2xl font-bold">Algoritmo actual: {algoritmoActual.nombre} </h4>
      <Matrix initialMatrix={initialMatrix} cellSize={CELL_SIZE} path={path}/>
    </>
  );
}

export default PathAnimation;