// Простая демонстрация подключения кошелька (заглушка)
// Ничего не делает на самом блокчейне

document.addEventListener('DOMContentLoaded', () => {
  const connectButton = document.getElementById('connect-wallet') || 
                       document.createElement('button');
  
  if (!document.getElementById('connect-wallet')) {
    connectButton.id = 'connect-wallet';
    connectButton.textContent = 'Connect Phantom';
    connectButton.style.padding = '12px 24px';
    connectButton.style.background = '#8b5cf6';
    connectButton.style.color = 'white';
    connectButton.style.border = 'none';
    connectButton.style.borderRadius = '8px';
    connectButton.style.cursor = 'pointer';
    document.body.appendChild(connectButton);
  }

  connectButton.addEventListener('click', async () => {
    if (window.solana && window.solana.isPhantom) {
      try {
        await window.solana.connect();
        alert('Кошелёк подключён (демонстрация)\nАдрес: ' + 
              window.solana.publicKey.toString().slice(0,6) + '...');
      } catch (err) {
        alert('Ошибка подключения: ' + err.message);
      }
    } else {
      alert('Пожалуйста, установите Phantom Wallet');
    }
  });
});