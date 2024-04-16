import { getCellImage } from "./Images";

export const Cell = ({ value, cellSize }) => {
    const image = getCellImage(value);
    const bg = value === 1 ? '#707070' : '#ffffff' 
    const cellStyle = {
        width: cellSize,
        height: cellSize,
        backgroundColor: bg,
    };


    return (
        <div style={cellStyle}>
        {image && (
            <img
            src={image.src}
            alt={`Cell ${value}`}
            style={{ maxWidth: "100%", maxHeight: "100%" }}
            />
        )}
        </div>
    );
};
