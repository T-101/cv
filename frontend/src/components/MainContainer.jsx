import React from 'react'
import Navbar from './Navbar'
import {ConfigContext} from "../contexts/ConfigContext"
import RouterComponent from "./RouterContainer";

export default function MainContainer() {
    const {windowIsWide} = React.useContext(ConfigContext)
    return (
        <div className={windowIsWide ? "container" : ""}>
            <RouterComponent>
                <Navbar/>
            </RouterComponent>
        </div>
    )
}
