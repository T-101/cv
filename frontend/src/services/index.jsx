export default async function fetchData() {
    const url = getRootURL() + process.env.REACT_APP_API_ENDPOINT
    let res = await fetch(url, {
        method: "GET"
    })
    if (res.status === 200 || res.status === 401) {
        return await res.json()
    }
}

function getHostname() {
    return process.env.NODE_ENV === "development" ? window.location.hostname : process.env.REACT_APP_API_HOSTNAME
}

function getPort() {
    const hostname = getHostname()
    return (hostname === 'localhost' || hostname === '127.0.0.1' || hostname === "0.0.0.0") ? ':8000' : ''
}

export function getRootURL() {
    return window.location.protocol + "//" + getHostname() + getPort()
}
