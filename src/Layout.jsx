import { useEffect } from "react";
import PathAnimation from "./Animation"
import Resultados from "./Resultados"
import SeleccionAlgoritmos from "./SeleccionAlgoritmos"
import { useStore } from "./useStore";

const Layout = () => {
    const { guardarResultados } = useStore();

    useEffect(() => {
        guardarResultados({a:"a", b:"b"})
    }, [])
    
    
    return (
        <>
            <div className="h-screen overflow-hidden grid grid-cols-2">
                <div className="h-full flex flex-col gap-4 justify-center items-center">
                    <PathAnimation />
                </div>
                
                <div className="grid" style={{ gridAutoRows: 'auto' }}>
                    <div className="flex flex-col justify-center items-center">
                        <SeleccionAlgoritmos />
                    </div>
                    <div className="flex flex-col justify-center items-center">
                        <Resultados />
                    </div>
                </div>
            </div>
        </>
    )
} 

export default Layout