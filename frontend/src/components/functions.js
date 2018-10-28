export async function getData(url) {
        try {
            return await (await(fetch(url))).json();
        }

        catch (e) {
            console.log("CATCHED ERROR", e);
        }
    }
