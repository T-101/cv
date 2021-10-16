import React, {useEffect} from 'react'
import fetchData from "../services"

export const DataContext = React.createContext({})

export function DataProvider(props) {
    const [data, setData] = React.useState(null)

    useEffect(() => {
        async function fetchFromAPI() {
            let res = await fetchData()
            setData(res)
        }

        fetchFromAPI()
    }, [])

    const state = {
        data: data,
    }

    return (
        <DataContext.Provider value={state}>
            {props.children}
        </DataContext.Provider>
    )
}

export const DataConsumer = DataContext.Consumer
