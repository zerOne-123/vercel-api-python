const axios = require('axios');
const CryptoJS = require('crypto-js');

var key = CryptoJS.enc.Utf8.parse('0123456789abcdef');
var iv = CryptoJS.enc.Utf8.parse('0123456789abcdef');

function AES_Encrypt(word) {
  var srcs = CryptoJS.enc.Utf8.parse(word);
  var encrypted = CryptoJS.AES.encrypt(srcs, key, {
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7,
  });
  return encrypted.toString();
}

function AES_Decrypt(word) {
  var srcs = word;
  var decrypt = CryptoJS.AES.decrypt(srcs, key, {
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7,
  });
  return decrypt.toString(CryptoJS.enc.Utf8);
}

module.exports = async (req, res) => {
  // const { name = 'js' } = req.query;
  // const html = await axios.get('https://www.baidu.com').then((res) => {
  //   return res.data;
  // });
  let html = 'error';
  // try {
  //   html = await axios.get('https://zxzj.vip');
  //   html = html.data;
  // } catch (error) {
  //   console.log(error);
  // }
  return res.send(AES_Encrypt('hello'));
};