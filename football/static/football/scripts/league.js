import { renderLineup, renderStats, renderEvents } from './templates.js';

// init match-handler
document
  .getElementById('league-table-container')
  .addEventListener('click', onLeagueTableClick);

function onLeagueTableClick(e) {
  const cell = e.target.closest('.match-cell');
  if (!cell) return;
  fetchMatchAndOpenModal(cell.id);
}

function fetchMatchAndOpenModal(matchId) {
  fetch(`/api/matches/${matchId}/`)
    .then(res => {
      if (!res.ok) throw new Error(`Status ${res.status}`);
      return res.json();
    })
    .then(openModal)
    .catch(err => {
      console.error(err);
      alert('Не удалось загрузить данные матча');
    });
}

// переключение вкладок и закрытие модалки
const modal       = document.getElementById('modal');
const modalClose  = document.getElementById('modal-close');
const modalContent= document.querySelector('.modal-content');
const tabButtons  = document.querySelectorAll('.tab-button');

const teamsNode   = document.getElementById('modal-teams');
const scoreNode   = document.getElementById('modal-score');
const lineupTab   = document.getElementById('tab-lineup');
const statsTab    = document.getElementById('tab-stats');
const eventsTab   = document.getElementById('tab-events');

tabButtons.forEach(btn => btn.addEventListener('click', onTabClick));
modalContent.addEventListener('click', e => e.stopPropagation());
modalClose.addEventListener('click', () => modal.classList.remove('active'));
modal.addEventListener('click', () => modal.classList.remove('active'));

function onTabClick(e) {
  e.preventDefault();
  tabButtons.forEach(b => b.classList.remove('active'));
  e.currentTarget.classList.add('active');
  document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
  document.getElementById('tab-' + e.currentTarget.dataset.tab).classList.add('active');
}

// Функция открытия и заполнения модалки
function openModal(data) {
  teamsNode.textContent = `${data.home_team_name} — ${data.guest_team_name}`;
  scoreNode.textContent = `${data.home_team_goals} : ${data.guest_team_goals}`;

  // Состав
  lineupTab.innerHTML = '';
  lineupTab.append(renderLineup(data));

  // Статистика
  statsTab.innerHTML = renderStats(data);

  // Ход матча
  eventsTab.innerHTML = renderEvents(data);

  modal.classList.add('active');
};

// переключение навигационных вкладок
document.querySelectorAll('.nav-tab').forEach(btn => {
  btn.addEventListener('click', e => {
        const navTabs     = document.querySelectorAll('.nav-tab');
        const tabContents = document.querySelectorAll('.nav-tab-content');

        navTabs.forEach(tab => {
          tab.addEventListener('click', e => {
            // снимаем активность со всех табов и контента
            navTabs.forEach(t => t.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            // активируем кликнутый таб и соответствующий контент
            e.currentTarget.classList.add('active');
            document
              .getElementById(e.currentTarget.dataset.target)
              .classList.add('active');
          });
        });
  });
});