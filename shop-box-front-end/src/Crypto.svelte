<style>
    section {
        margin: auto;
        width: 60rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    }
    .chart{
        width: 100%;
        height: 370px;
        margin-bottom: 20px;
        -webkit-box-shadow: 0px 15px 50px 0px rgba(160, 163, 189, 0.1);
        box-shadow: 0px 15px 50px 0px rgba(160, 163, 189, 0.1);
    }
</style>
<script>
    let result;
    window.onload = function(){
    let url = 'http://localhost:8000/api/market_info';
    let xmlHttp = new XMLHttpRequest();
    setInterval(() => {
        xmlHttp.onreadystatechange = function(){
        if (xmlHttp.status == 200 && xmlHttp.readyState == 4)
        result = JSON.parse(xmlHttp.response);
    }
    xmlHttp.open('GET',url);
    xmlHttp.send();
    }, 5000);
}

</script>
<section>
    {#if result}
    <div>
        <label for="">BTC</label>
        <label for="price">{result[0]["metrics"]["market_data"]["price_usd"].toFixed(2)}</label>
    </div>
    {/if}
    <div class="chart">
        <canvas id="mchart"></canvas>
    </div>
</section>
<section >
    {#if result}
    <div class="table">
        <table>
            <thead>
                <tr>
                    <th>Crypto Name</th>
                    <th>Price ($)</th>
                </tr>
            </thead>
            <tbody>
                    {#each result as index}
                        <tr>
                            <td>{index['symbol']}</td>
                            <td>{index["metrics"]["market_data"]["price_usd"].toFixed(2)}</td>
                        </tr>
                    {/each}
            </tbody>

        </table>
    </div>
    {/if}
</section>

