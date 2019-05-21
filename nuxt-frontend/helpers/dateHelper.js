module.exports = {
  getDate: function(val) {
    val = 0 | ((Date.now() - val) / 1000)
    let unit
    const length = {
      sec: 60,
      min: 60,
      hr: 24,
      day: 7,
      week: 4.35,
      month: 12,
      year: 10000
    }
    let result

    for (unit in length) {
      result = val % length[unit]
      if (!(val = 0 | (val / length[unit])))
        return result + ' ' + (result - 1 ? unit + 's' : unit)
    }
  }
}
