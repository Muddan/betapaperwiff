module.exports = {
  getDate: function(date) {
    const mlist = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December'
    ]
    const curDate = new Date(date)
    return `${curDate.getDate()}, ${
      mlist[curDate.getMonth()]
    } ${curDate.getFullYear()}`
  }
}
