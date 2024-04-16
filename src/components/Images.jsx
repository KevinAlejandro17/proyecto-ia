const nave = new Image();
const mando = new Image();
const grogu = new Image();
const trooper = new Image();

nave.src = "src/assets/nave.png";
mando.src = "src/assets/mando.png";
grogu.src = "src/assets/grogu.png";
trooper.src = "src/assets/trooper.png";

export const getCellImage = (value) => {
    switch (value) {
        case 0:
            return null;
        case 1:
            return null; 
        case 2:
            return mando;
        case 3:
            return nave;
        case 4:
            return trooper;
        case 5:
            return grogu;
        default:
            return null;
        }
};