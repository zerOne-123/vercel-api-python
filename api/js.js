const axios = require('axios').default;

module.exports = async (req, res) => {
  const { name = 'js' } = req.query;
  // const html = await axios.get('https://www.baidu.com').then((res) => {
  //   return res.data;
  // });
  const html = await axios.get('https://www.baidu.com')
  return res.send(html);
};
