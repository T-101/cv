export default function lol_decrypt(str) {
    const input = 'o8MVAcyfZxar3vFzbeBOhL+RYQTCI-i@U9dGs2w5gNDp4S6EHu0WlqtP.K_1kj7nXJm';
    const output = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-@_.";
    const index = x => input.indexOf(x);
    const translate = x => index(x) > -1 ? output[index(x)] : x;
    return str.split('').map(translate).join('');
}
