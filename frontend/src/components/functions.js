export async function getData(url) {
        try {
            return await (await(fetch(url))).json();
        }

        catch (e) {
            console.log("CATCHED ERROR", e);
        }
    }

export function getUrl(endPoint) {
    const protocol = window.location.protocol;
    const hostname = window.location.hostname;
    const port = (hostname === 'localhost' || hostname === '127.0.0.1') ? ':8000' : '';
    const baseUrl = protocol + '//' + hostname + port;
    switch (endPoint) {
        case 'me': {
            return baseUrl + '/api/v1/info/info/me/'
        }
        case 'random': {
            return baseUrl + '/api/v1/info/pictures/random/'
        }
        case 'hobbies': {
            return baseUrl + '/api/v1/hobby/hobbies/'
        }
        case 'details': {
            return baseUrl + '/api/v1/info/details/'
        }
        case 'work': {
            return baseUrl + '/api/v1/cv/pier/'
        }
        default:
    }
}
