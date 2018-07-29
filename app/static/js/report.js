$(document).ready(function(){
    var budgets = [];
    var expenses_map = {};
    var dialogBudget = $('#newBudget').get(0);
    var dialogExpense = $('#newExpense').get(0);
    dialogPolyfill.registerDialog(dialogBudget);
    dialogPolyfill.registerDialog(dialogExpense);
    
    $.ajax({
        type : 'GET',
        url : '/budget/all',
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            if (result.length > 0) { 
                budgets = result;
                console.log(budgets);
                barChart('budgets', budgets, 'name');
                budgetDropdown(budgets);
                budgetClick()
            }
        }
    });

    $.ajax({
        type : 'GET',
        url : '/expense/all',
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            expense_totals = [];
            if (Object.keys(result).length > 0) {
                expenses_map = result;
                barChart('expenses', expenses_map[$('#budgetList').val()], 'description');
                expenseClick();
            }
        }
    });

    $('#budgetList').change(function(){
        console.log($('#budgetList').val())
        console.log(expenses_map)
        console.log(expenses_map[$('#budgetList').val()])
        barChart('expenses', expenses_map[$('#budgetList').val()], 'description');
    });

    $('#newBudgetButton').click(function(){
        dialogBudget.showModal();
    });

    $('#newBudgetClose').click(function(){
        dialogBudget.close();
        clear($('#budgetName'), $('#newAmount'));
    });

    $('#newExpenseButton').click(function(){
        dialogExpense.showModal();
    });

    $('#newExpenseClose').click(function(){
        dialogExpense.close();
        clear($('#expenseName'), $('#newExpenseAmount'));
    });

    $('#newBudgetCreate').click(function(evt){
        var bName = $('#budgetName').val(),
            bAmount = $('#newAmount').val();
        var payload = {'name': bName, 'amount': bAmount};
        clear($('#budgetName'), $('#newAmount'));
        $.ajax({
                type : 'POST',
                url : '/budget/new',
                data: JSON.stringify(payload, null, '\t'),
                contentType: 'application/json;charset=UTF-8',
                success: function(result) {
                    dialogBudget.close();
                    budgets.push(result);
                    barChart('budgets', budgets, 'name');
                    budgetDropdown(budgets);
                    budgetClick();
                },
                error: function(data) {
                    alert(data.responseText);
                }
            });
    });

    $('#newExpenseCreate').click(function(evt){

        var bName = $('#expenseName').val(),
            bAmount = $('#newExpenseAmount').val(),
            budgetId = $('#budgetList').val();
        var payload = {'name': bName, 'amount': bAmount, 'budget_id': budgetId};
        clear($('#expenseName'), $('#newExpenseAmount'));
        $.ajax({
                type : 'POST',
                url : '/expense/new',
                data: JSON.stringify(payload, null, '\t'),
                contentType: 'application/json;charset=UTF-8',
                async: false,
                success: function(result) {
                    dialogExpense.close();
                    var tempBool = false;
                    budgets[result.budget_id-1].amount -= result.amount;
                    if (expenses_map.hasOwnProperty(result.budget_id)) {
                        var expense = expenses_map[result.budget_id];
                        for (var i = 0; i < expense.length; ++i) {
                            if (expense[i].description === result.description) {
                                expense[i].amount += result.amount;
                                tempBool = true;
                                console.log(expenses_map);
                            }
                        }
                        if (!tempBool) {
                            expenses_map[result.budget_id].push(result)
                        }
                    }
                    else {
                        expenses_map[result.budget_id] = [];
                        expenses_map[result.budget_id].push(result)  
                    }
                    barChart('expenses', expenses_map[result.budget_id], 'description')
                    barChart('budgets', budgets, 'name')
                    budgetClick();
                    expenseClick();
                },
                error: function(data) {
                    alert(data.responseText);
                }
            });
            evt.stopPropagation();
    });

    $('#downloadBtn').click(function(evt) {
        var doc = new jsPDF();
        doc.setFontSize(40);
        doc.myText(`Budget Report for: ${budgets[$('#budgetList').val()-1].name}`, {align: 'center'} , 35, 25);
        doc.myText(`Initial Amount: ${budgets[$('#budgetList').val()-1].intial_amount}`, {align: 'center'} , 35, 42);
        doc.myText(`Amount Remaining: ${budgets[$('#budgetList').val()-1].amount}`, {align: 'center'}, 35, 60);
        doc.myText('Expenses:', {align: 'center'}, 35, 78);

        Plotly.toImage(document.getElementById('expenses'), {format: 'png', width: 800, height: 600}).then(function(dataUrl) {
            doc.addImage(dataUrl, 'PNG' , 10, 80, 200, 150);
            doc.save(`${budgets[$('#budgetList').val()-1].name}-report.pdf`);
        });
    });

    function budgetDropdown(budgets) {
        $('#budgetList').html('');
        $.each(budgets, function(index, value){
            $('#budgetList').append(`<option value="${value.id}">${value.name}</option>`)
        });
    }

    function budgetClick() {
        document.getElementById('budgets').on('plotly_click', function(data){
            var deleteBudget = confirm(`Delete budget ${data.points[0].y}?`);
            if (deleteBudget) {
                var payload = {'name': data.points[0].y};
                $.ajax({
                        type : 'POST',
                        url : '/budget/delete',
                        data: JSON.stringify(payload, null, '\t'),
                        contentType: 'application/json;charset=UTF-8',
                        async: false,
                        success: function(result) {
                            budgets = budgets.slice(result);
                            expenses_map[result] = [];
                            barChart('expenses', expenses_map[result], 'description');
                            barChart('budgets', budgets, 'name');
                            budgetDropdown(budgets);
                            budgetClick();
                            expenseClick();
                        }
                });
            } 
        });
    }

    function expenseClick() {
        document.getElementById('expenses').on('plotly_click', function(data){
            var deleteExpense = confirm(`Delete expense ${data.points[0].y}?`);
            if (deleteExpense) {
                var payload = {'name': data.points[0].y};
                $.ajax({
                        type : 'POST',
                        url : '/expense/delete',
                        data: JSON.stringify(payload, null, '\t'),
                        contentType: 'application/json;charset=UTF-8',
                        async: false,
                        success: function(result) {
                            expense = expenses_map[result][0];
                            console.log(expense);
                            budgets[result-1].amount += expense.amount;
                            expenses_map[result] = [];
                            console.log(budgets);
                            barChart('expenses', expenses_map[result], 'description');
                            barChart('budgets', budgets, 'name')
                            budgetClick();
                            expenseClick();
                        }
                });
            } 
        });
    }

    function clear(text1, text2) {
        text1.val('');
        text2.val('');
    }
});
