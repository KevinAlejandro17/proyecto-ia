import { useEffect, useState } from "react";
import { Cell } from "./Cell";
import { findStartPosition } from "../Utils";
import { useStore } from "../useStore";

const directions = {
    derecha: [0, 1],
    izquierda: [0, -1],
    arriba: [-1, 0],
    abajo: [1, 0]
};

export const Matrix = ({ initialMatrix, cellSize, path }) => {
    const [matrix, setMatrix] = useState(initialMatrix);
    const [pathIndex, setPathIndex] = useState(0);
    const [prevPoint, setPrevPoint] = useState(findStartPosition(initialMatrix));
    const [prevValue, setPrevValue] = useState(null);

    const [animationKey, setAnimationKey] = useState(0);

    useEffect(() => {
        if (!path) return;

        const interval = setInterval(() => {
            if (pathIndex < path.length) {
                const [dx, dy] = directions[path[pathIndex]];
                const [prevRow, prevCol] = prevPoint;
                const [row, col] = [prevRow + dx, prevCol + dy];

                const newMatrix = matrix.map(row => [...row]);
                if (prevPoint) {
                    newMatrix[prevRow][prevCol] = prevValue;
                }

                const currentValue = newMatrix[row][col];
                newMatrix[row][col] = 2;

                setMatrix(newMatrix);
                setPrevPoint([row, col]);
                setPrevValue(currentValue);
                setPathIndex(pathIndex + 1);
            }
        }, 200);

        return () => clearInterval(interval);
    }, [pathIndex, path, matrix]);

    const { algoritmoActual } = useStore();

    useEffect(() => {
        const restartAnimation = () => {
            setMatrix(initialMatrix);  
            setPathIndex(0);
            setPrevPoint(findStartPosition(initialMatrix))
            setPrevValue(null);       
            setAnimationKey(prevKey => prevKey + 1);  
        };

        algoritmoActual && restartAnimation();
      
    }, [algoritmoActual])
    
    


    return (
        <div key={animationKey} style={{
            display: "grid",
            gridTemplateColumns: `repeat(${matrix[0].length}, ${cellSize}px)`,
            gridGap: "1px",
        }}>
        {matrix.map((row, rowIndex) =>
            row.map((cell, cellIndex) => (
            <Cell key={`${rowIndex}-${cellIndex}`} value={cell} cellSize={cellSize} />
            ))
        )}
        </div>
    );
};