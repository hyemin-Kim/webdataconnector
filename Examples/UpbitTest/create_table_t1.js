(function() {
    // Create the connector object
    var myConnector = tableau.makeConnector();

    // Define the schema
    myConnector.getSchema = function(schemaCallback) {
		var cols = [{
            id: "market",
            dataType: tableau.dataTypeEnum.String
        }, {
            id: "candle_date_time_kst",
            alias: "date",
            dataType: tableau.dataTypeEnum.date
        }];

        var tableSchema = {
            id: "upbit",
            alias: "upbit data test",
            columns: cols
        };

        schemaCallback([tableSchema]);
    };

    // Download the data
    myConnector.getData = function(table, doneCallback) {
        $.getJSON("https://raw.githubusercontent.com/hyemin-Kim/webdataconnector/master/Examples/UpbitTest/upbit_data_t1.json", function(resp) {
            var feat = resp,
                tableData = [];

            // Iterate over the JSON object
            for (var i = 0, len = feat.length; i < len; i++) {
                tableData.push({
			"market": feat[i].market,
            		"candle_date_time_kst": feat[i].candle_date_time_kst
                });
            }

            table.appendRows(tableData);
            doneCallback();
        });
    };

    tableau.registerConnector(myConnector);

    // Create event listeners for when the user submits the form
    $(document).ready(function() {
        $("#submitButton").click(function() {
            tableau.connectionName = "upbit data test"; // This will be the data source name in Tableau
            tableau.submit(); // This sends the connector object to Tableau
        });
    });
})();
