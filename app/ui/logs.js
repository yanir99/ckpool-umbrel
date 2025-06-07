fetch('/api/logs')
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById('log-list');
        data.logs.forEach(log => {
            const item = document.createElement('li');
            item.textContent = log;
            item.onclick = () => {
                fetch('/api/logs/' + log)
                    .then(res => res.text())
                    .then(text => {
                        document.getElementById('log-content').textContent = text;
                    });
            };
            list.appendChild(item);
        });
    });
