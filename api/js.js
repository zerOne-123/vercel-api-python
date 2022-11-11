const axios = require('axios');

module.exports = async (req, res) => {
  // const { name = 'js' } = req.query;
  // const html = await axios.get('https://www.baidu.com').then((res) => {
  //   return res.data;
  // });
  let html = 'error'
  try {
    html = await axios.get('https://zxzj.vip');
    html = html.data
  } catch (error) {
    console.log(error);
  }
  return res.send(html);
};
