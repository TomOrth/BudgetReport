$(document).ready(function(){
    var budgets = [];
    var expenses_map = {};
    var dialogBudget = $('#newBudget').get(0);
    var dialogExpense = $('#newExpense').get(0);
    dialogPolyfill.registerDialog(dialogBudget);
    dialogPolyfill.registerDialog(dialogExpense);
    
    $.ajax({
        type : 'GET',
        url : '/budget/budgets',
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            if (result.length > 0) { 
                budgets = result;
                console.log(budgets);
                barChart('budgets', budgets, 'name');
                budgetDropdown(budgets);
            }
        }
    });

    $.ajax({
        type : 'GET',
        url : '/expense/expenses',
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            expense_totals = [];
            if (Object.keys(result).length > 0) {
                expenses_map = result;
                barChart('expenses', expenses_map[$('#budgetList').val()], 'description');
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
    });

    $('#newExpenseButton').click(function(){
        dialogExpense.showModal();
    });

    $('#newExpenseClose').click(function(){
        dialogExpense.close();
    });

    $('#newBudgetCreate').click(function(evt){
        var bName = $('#budgetName').val(),
            bAmount = $('#newAmount').val();
        var payload = {'name': bName, 'amount': bAmount};
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
                }
            });
    });

    $('#newExpenseCreate').one('click', function(evt){

        var bName = $('#expenseName').val(),
            bAmount = $('#newExpenseAmount').val(),
            budgetId = $('#budgetList').val();
        var payload = {'name': bName, 'amount': bAmount, 'budget_id': budgetId};
        $.ajax({
                type : 'POST',
                url : '/expense/new',
                data: JSON.stringify(payload, null, '\t'),
                contentType: 'application/json;charset=UTF-8',
                async: false,
                success: function(result) {
                    dialogExpense.close();
                    console.log(budgets);
                    console.log(budgets[result.budget_id]);
                    console.log(result);
                    budgets[result.budget_id-1].amount -= result.amount;
                    if (expenses_map.hasOwnProperty(result.budget_id)) {
                        expenses_map[result.budget_id].push(result)
                    }
                    else {
                        expenses_map[result.budget_id] = [];
                        expenses_map[result.budget_id].push(result)  
                    }
                    barChart('expenses', expenses_map[result.budget_id], 'description')
                    barChart('budgets', budgets, 'name')
                }
            });
            evt.stopPropagation();
    });

    function budgetDropdown(budgets) {
        $('#budgetList').html('');
        $.each(budgets, function(index, value){
            $('#budgetList').append(`<option value="${value.id}">${value.name}</option>`)
        });
    }
});
