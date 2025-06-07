function saveConfig() {
    const content = document.getElementById('config').value;
    fetch('/api/config', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content })
    }).then(res => res.json()).then(console.log);
}

fetch('/api/config')
    .then(res => res.json())
    .then(data => {
        if (data.content) {
            document.getElementById('config').value = data.content;
        }
    });
