import React from 'react'
import {ConfigProvider} from "../contexts/ConfigContext"
import {DataProvider} from "../contexts/DataContext";

export default function ContextContainer(props) {
    return (
        <ConfigProvider>
            <DataProvider>
                {props.children}
            </DataProvider>
        </ConfigProvider>
    )
}
