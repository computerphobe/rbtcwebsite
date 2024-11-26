// Safely check and parse chart data
document.addEventListener('DOMContentLoaded', function() {
    // Ensure Chart.js is loaded
    if (typeof Chart !== 'undefined') {
        // Bar Chart
        const barChartEl = document.getElementById('barChart');
        if (barChartEl) {
            const barCtx = barChartEl.getContext('2d');
            
            // Safely parse and validate data
            const pendingCount = parseInt('{{ pending_components|length }}') || 0;
            const issuedCount = parseInt('{{ issued_components|length }}') || 0;
            const returnedCount = parseInt('{{ returned_components|length }}') || 0;

            new Chart(barCtx, {
                type: 'bar',
                data: {
                    labels: ['Pending', 'Issued', 'Returned'],
                    datasets: [{
                        label: 'Components Count',
                        data: [pendingCount, issuedCount, returnedCount],
                        backgroundColor: [
                            'rgba(255, 204, 0, 0.7)',   // Soft yellow
                            'rgba(76, 175, 80, 0.7)',   // Soft green
                            'rgba(33, 150, 243, 0.7)'   // Soft blue
                        ],
                        borderColor: [
                            'rgba(255, 204, 0, 1)',
                            'rgba(76, 175, 80, 1)',
                            'rgba(33, 150, 243, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: { 
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Components'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Component Status Distribution'
                        }
                    }
                }
            });
        }

        // Pie Chart
        const pieChartEl = document.getElementById('pieChart');
        if (pieChartEl) {
            const pieCtx = pieChartEl.getContext('2d');
            
            // Safely parse and validate data
            const pendingCount = parseInt('{{ pending_components|length }}') || 0;
            const issuedCount = parseInt('{{ issued_components|length }}') || 0;
            const returnedCount = parseInt('{{ returned_components|length }}') || 0;

            new Chart(pieCtx, {
                type: 'pie',
                data: {
                    labels: ['Pending', 'Issued', 'Returned'],
                    datasets: [{
                        data: [pendingCount, issuedCount, returnedCount],
                        backgroundColor: [
                            'rgba(255, 204, 0, 0.7)',   // Soft yellow
                            'rgba(76, 175, 80, 0.7)',   // Soft green
                            'rgba(33, 150, 243, 0.7)'   // Soft blue
                        ],
                        hoverOffset: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Component Status Breakdown'
                        },
                        legend: {
                            position: 'bottom'
                        }
                    }
                }
            });
        }
    } else {
        console.error('Chart.js library is not loaded');
    }
});