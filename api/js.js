const axios = require('axios');

module.exports = async (req, res) => {
  const { name = 'js' } = req.query;
  // const html = await axios.get('https://www.baidu.com').then((res) => {
  //   return res.data;
  // });
  const html = {}
  try {
    html = await axios.get('https://zxzj.vip');
  } catch (error) {
    console.log(error);
  }
  res.json(html);
};
