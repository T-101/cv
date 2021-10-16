import React from 'react';

export const ConfigContext = React.createContext({});

export function ConfigProvider(props) {
    const [width, setWidth] = React.useState(window.innerWidth)
    // eslint-disable-next-line no-unused-vars
    const [responsiveBreakpoint, setResponsiveBreakpoint] = React.useState(640)

    function updateWindowDimensions() {
        setWidth(window.innerWidth)
    }

    const windowIsWide = width >= responsiveBreakpoint

    React.useEffect(() => {
        updateWindowDimensions()
        window.addEventListener('resize', updateWindowDimensions)

        return function cleanup() {
            window.removeEventListener('resize', updateWindowDimensions)
        }
    }, [])

    const state = {
        windowIsWide: windowIsWide
    };

    return (
        <ConfigContext.Provider value={state}>
            {props.children}
        </ConfigContext.Provider>
    );
}

export const ConfigConsumer = ConfigContext.Consumer;
