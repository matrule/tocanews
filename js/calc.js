/* The licence calculator in a Learn article: a <div data-calc> holding two tables. The first asks about the firm:
   each td.q[data-in] holds an example number under a name. The second is the bill: each body row carries data-price
   (pounds per licence per month) and data-from (the names to multiply, joined by *), with td.n for the number of
   licences and td.y for the year's cost; [data-total] cells take m, y and y3. The page reads correctly without this
   script (the example, worked out by hand); the script turns each number into a field and keeps the sums live.
   Every string goes in through textContent. */
(function () {
  function money(p) {
    var pounds = Math.floor(p / 100), pence = p % 100;
    return '£' + pounds.toLocaleString('en-GB') + (pence ? '.' + (pence < 10 ? '0' : '') + pence : '');
  }
  document.querySelectorAll('[data-calc]').forEach(function (box) {
    var fields = {}, list = [];
    box.querySelectorAll('td.q[data-in]').forEach(function (q) {
      var start = parseInt(q.textContent, 10) || 0;
      var input = document.createElement('input');
      input.type = 'number'; input.min = '0'; input.max = '100000'; input.step = '1'; input.inputMode = 'numeric';
      input.value = String(start);
      input.setAttribute('aria-label', q.getAttribute('data-label') || 'Number');
      q.textContent = ''; q.appendChild(input);
      var f = { input: input, start: start };
      fields[q.getAttribute('data-in')] = f; list.push(f);
    });
    var rows = [];
    box.querySelectorAll('tbody tr[data-price][data-from]').forEach(function (tr) {
      var price = Math.round(parseFloat(tr.getAttribute('data-price')) * 100);
      var from = tr.getAttribute('data-from').split('*');
      var n = tr.querySelector('td.n'), y = tr.querySelector('td.y');
      if (!n || !y || !(price > 0) || !from.every(function (k) { return fields[k]; })) return;
      rows.push({ price: price, from: from, n: n, y: y });
    });
    if (!list.length || !rows.length) return;
    var totals = {};
    box.querySelectorAll('[data-total]').forEach(function (el) { totals[el.getAttribute('data-total')] = el; });
    function val(k) {
      var n = Math.floor(Number(fields[k].input.value));
      return n > 0 ? Math.min(n, 100000) : 0;
    }
    function sum() {
      var month = 0;
      rows.forEach(function (r) {
        var n = r.from.reduce(function (a, k) { return a * val(k); }, 1);
        r.n.textContent = n.toLocaleString('en-GB');
        r.y.textContent = money(n * r.price * 12);
        month += n * r.price;
      });
      if (totals.m) totals.m.textContent = money(month);
      if (totals.y) totals.y.textContent = money(month * 12);
      if (totals.y3) totals.y3.textContent = money(month * 36);
    }
    box.addEventListener('input', sum);
    var reset = document.createElement('button');
    reset.type = 'button'; reset.textContent = 'Back to the example';
    reset.addEventListener('click', function () { list.forEach(function (f) { f.input.value = String(f.start); }); sum(); });
    var p = document.createElement('p'); p.className = 'calc-reset'; p.appendChild(reset);
    box.appendChild(p);
    sum();
  });
})();
