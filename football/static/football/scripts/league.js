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

const apiUrl = '/api/players';
let playersData = [];
let currentPage = 1;
const rowsPerPage = 50;
let currentSortKey = '';
let currentSortOrder = 'asc';

document.addEventListener('DOMContentLoaded', () => {
  fetchPlayers();
  setupSorting();
});

function fetchPlayers() {
  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      playersData = data;
      renderTable();
      renderPagination();
    })
    .catch(error => console.error('Ошибка при получении данных:', error));
}

function setupSorting() {
  document.querySelectorAll('#playersTable th').forEach(header => {
    header.addEventListener('click', () => {
      const key = header.getAttribute('data-key');
      sortBy(key);
    });
  });
}

function sortBy(key) {
  if (currentSortKey === key) {
    currentSortOrder = currentSortOrder === 'asc' ? 'desc' : 'asc';
  } else {
    currentSortKey = key;
    currentSortOrder = 'asc';
  }
  playersData.sort((a, b) => {
    if (a[key] < b[key]) return currentSortOrder === 'asc' ? -1 : 1;
    if (a[key] > b[key]) return currentSortOrder === 'asc' ? 1 : -1;
    return 0;
  });
  currentPage = 1;
  renderTable();
  renderPagination();
}

function renderTable() {
  const tbody = document.querySelector('#playersTable tbody');
  tbody.innerHTML = '';
  const start = (currentPage - 1) * rowsPerPage;
  const end = start + rowsPerPage;
  const pageData = playersData.slice(start, end);

  pageData.forEach(player => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${player.name}</td>
      <td>${player.goals}</td>
      <td>${player.assists}</td>
      <td>${player.appearances}</td>
    `;
    tbody.appendChild(tr);
  });
}

function renderPagination() {
  const pagination = document.getElementById('pagination');
  pagination.innerHTML = '';
  const totalPages = Math.ceil(playersData.length / rowsPerPage);

  for (let i = 1; i <= totalPages; i++) {
    const btn = document.createElement('button');
    btn.innerText = i;
    if (i === currentPage) btn.classList.add('active');
    btn.addEventListener('click', () => {
      currentPage = i;
      renderTable();
      renderPagination();
    });
    pagination.appendChild(btn);
  }
}
