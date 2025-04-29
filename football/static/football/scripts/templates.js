// static/js/templates.js

// Собираем HTML для «Состав»
export function renderLineup(data) {
  const container = document.createElement('div');
  container.className = 'lineup-container';

  ['home_lineup', 'guest_lineup'].forEach((teamKey, idx) => {
    const pitch = document.createElement('div');
    pitch.className = 'pitch formation-433';

    const lineup = data[teamKey];
    // Позиции в формате { index, css-свойства }
    const positions = [
      { index: 0, style: 'bottom: 5%; left: 50%; transform: translateX(-50%);' },  // Вратарь
      { index: 1, style: 'bottom: 20%; left: 5%;' },  // Левый защитник
      { index: 2, style: 'bottom: 20%; left: 35%;' },  // Левый центральный защитник
      { index: 3, style: 'bottom: 20%; left: 65%;' },  // Правый центральный защитник
      { index: 4, style: 'bottom: 20%; left: 85%;' },  // Правый защитник
      { index: 5, style: 'bottom: 45%; left: 20%;' },  // Левый полузащитник
      { index: 6, style: 'bottom: 45%; left: 50%; transform: translateX(-50%);' },  // Центральный полузащитник
      { index: 7, style: 'bottom: 45%; left: 70%;' },  // Правый полузащитник
      { index: 8, style: 'bottom: 70%; left: 15%;' },  // Левый нападающий
      { index: 9, style: 'bottom: 80%; left: 50%; transform: translateX(-50%);' },  // Центральный нападающий
      { index: 10, style: 'bottom: 70%; left: 75%;' },  // Правый нападающий
    ];

    positions.forEach(pos => {
      const player = document.createElement('div');
      player.className = 'player';
      player.textContent = lineup[pos.index] || '';
      // inline стили для позиционирования и отображения
      player.style.position = 'absolute';
      player.style.cssText += pos.style + 'padding:4px 6px; font-size:0.75rem; color:#fff; background:rgba(0,0,0,0.6); border-radius:4px;';
      pitch.appendChild(player);
    });

    container.appendChild(pitch);
  });

  return container;
}


// HTML для «Статистика»
export function renderStats(data) {
  return `
    <table>
      <thead>
        <tr>
          <th>Показатель</th>
          <th>${data.home_team_name}</th>
          <th>${data.guest_team_name}</th>
        </tr>
      </thead>
      <tbody>
        ${Object.entries(data.stats).map(([k,v]) => `
          <tr>
            <td>${k}</td>
            <td>${v.home}</td>
            <td>${v.away}</td>
          </tr>`).join('')}
      </tbody>
    </table>`;
}

// HTML для «Ход матча»
export function renderEvents(data) {
  return `
    <ul class="event-list">
      ${data.events.map(ev => `
        <li>
          <strong>${ev.minute}'</strong>
          ${ev.team === 'home' ? data.home_team_name : data.guest_team_name}:
          ${ev.description}
        </li>`).join('')}
    </ul>`;
}
