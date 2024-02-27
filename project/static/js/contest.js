fetch('/data_javascript')
    .then(response => response.json())
    .then(data => {
        const contests = document.querySelectorAll('.datetime');

        data.forEach((time, index) => {
            const updateCountdown = () => {
            const targetDate = new Date(time).getTime();
            const now = new Date().getTime();
            const disTime = targetDate - now;
                
            if (disTime > 0) {
                    const days = Math.floor(disTime / (1000 * 60 * 60 * 24));
                    const hours = Math.floor((disTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    const minutes = Math.floor((disTime % (1000 * 60 * 60)) / (1000 * 60));
                    const seconds = Math.floor((disTime % (1000 * 60)) / 1000);
                    const formattedTime = ` 残り:${days}日 ${hours}時間 ${minutes}分 ${seconds}秒`;
                    console.log(formattedTime);
                    contests[index].innerText = formattedTime;
                } else {
                    contests[index].innerText = 'Contest Ended';
                }
            };
         
            // 最初の実行
            updateCountdown();
         
            // 1秒ごとに更新
            setInterval(updateCountdown, 1000);
         });
         
        });