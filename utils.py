dataset = """
Unnamed: 0,model_name,brand,processor_name,ram(GB),ssd(GB),Hard Disk(GB),Operating System,graphics,screen_size(inches),resolution (pixels),no_of_cores,no_of_threads,spec_score,price,cost,stock
291,Asus TUF Gaming A15 FA506ICB-HN005W Laptop,Asus,Ryzen 7 4800H,8,512,0,Windows,4 GB NVIDIA GeForce RTX 3050,15.6,1920 x 1080,8,16,68,69990,41994,120
906,Asus TUF Dash F15 2022 FX517ZE-HN036WS Gaming Laptop,Asus,12th Gen Core i7,16,512,0,Windows,4 GB NVIDIA GeForce RTX 3050-Ti,15.6,1920 x 1080,10,16,68,98990,69193,60
934,Asus VivoBook 15 X512DA-BQ303WS Laptop,Asus,Ryzen 3 3250U,8,256,0,Windows,AMD Radeon AMD Radeon,15.6,1920 x 1080,2,4,48,33990,23793,200
130,Asus VivoBook 15 X515EA-EJ522WS Laptop,Asus,11th Gen Core i5,8,512,0,Windows,Intel Integrated Iris Xe,15.6,1920 x 1080,4,8,61,46990,35193,150
634,Asus ROG Zephyrus G14 GA402RJZ-L4136WS Gaming Laptop,Asus,AMD Ryzen 9 6900HS,16,1000,0,Windows,8 GB AMD Radeon RX 6700S,14.0,1920 x 1080,8,16,82,155000,124000,30
288,Asus TUF Gaming F17 FX707ZM-HX030WS Laptop,Asus,12th Gen Core i7,16,1000,0,Windows,6 GB NVIDIA GeForce RTX 3060,17.3,1920 x 1080,14,20,76,109990,87992,40
916,Asus ROG Flow Z13 2022 GZ301ZE-LC192WS Gaming Laptop,Asus,12th Gen Core i9,16,1000,0,Windows,4 GB NVIDIA GeForce RTX 3050 Ti,13.4,3840 x 2400,14,20,72,191990,153592,25
131,Asus Vivobook 15 2022 X1502ZA-EZ311WS Touch Laptop,Asus,12th Gen Core i3,8,512,0,Windows,Intel Iris Xe,15.6,1920 x 1080,10,12,59,43879,35096,140
715,Asus ROG Strix Scar 17 SE G733CX-LL013WS Gaming Laptop,Asus,12th Gen Core i9,32,2000,0,Windows,16 GB NVIDIA GeForce RTX 3080 Ti,17.3,2560 x 1440,16,24,86,359990,287992,15
979,Asus Vivobook S15 OLED K3502ZA-L701WS Laptop,Asus,12th Gen Core i7,16,512,0,Windows,Intel Iris XE Graphics,15.6,1920 x 1080,14,20,71,84700,67760,70
808,Asus ROG Zephyrus G15 2022 GA503RM-LN143WS Gaming Laptop,Asus,AMD Ryzen 7 6800HS,16,1000,0,Windows,6 GB NVIDIA GeForce RTX 3060,15.6,2560 x 1440,8,16,84,144990,108742,50
411,Asus ROG Zephyrus G15 GA503RMZ-LN155WS Gaming Laptop,Asus,AMD Ryzen 7 6800HS,16,1000,0,Windows,6 GB NVIDIA GeForce RTX 3060,15.6,2560 x 1440,8,16,81,157990,110592,45
498,Asus VivoBook 15 2022 X515JA-EJ592WS Laptop,Asus,10th Gen Core i5,8,512,0,Windows,Intel Integrated UHD,15.6,1920 x 1080,4,8,59,44990,35992,130
121,Asus Chromebook Flip C214MA-BU0704 Laptop,Asus,Celeron N4020,4,0,32,Chrome,Intel Integrated UHD 600,11.6,1366 x 768,2,2,0,15990,12792,250
134,Asus TUF Gaming F15,Asus,2022) FX507ZE-HN038W Gaming Laptop ,16,512,0,Windows,4 GB NVIDIA GeForce RTX 3050-Ti,15.6,1920 x 1080,14,20,79,94990,75992,80
521,Asus Vivobook 14 OLED X1405ZA-KM311WS Laptop,Asus,12th Gen Core i3,8,512,0,Windows,Intel Iris Xe,14.0,2880 x 1800,6,8,56,51990,41592,100
911,Asus ROG Flow Z13 2022 GZ301ZE-LC193WS Gaming Laptop,Asus,12th Gen Core i9,16,1000,0,Windows,4 GB NVIDIA GeForce RTX 3050 Ti,13.4,3840 x 2400,14,20,74,304980,243984,20
519,Asus Vivobook 14 OLED X1405ZA-KM511WS Laptop,Asus,12th Gen Core i5,16,512,0,Windows,Intel Iris Xe,14.0,2880 x 1800,10,12,61,69990,55992,90
915,Asus TUF Dash F15 2022 FX517ZR-HQ030WS Gaming Laptop,Asus,12th Gen Core i7,16,1000,0,Windows,8 GB NVIDIA GeForce RTX 3070,15.6,2560 x 1440,10,16,74,149990,119992,55
811,Asus ROG Zephyrus G15 2022 GA503RS-HQ027WS Gaming Laptop,Asus,AMD Ryzen 9 6900HS,16,1000,0,Windows,8 GB NVIDIA GeForce RTX 3080,15.6,2560 x 1440,8,16,84,199086,159269,35
"""

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proposal</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            position: relative; /* Ensure the container is a positioned element */
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            position: relative; /* Ensure the container is a positioned element */
        }
        h1, h2 {
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #007bff; /* Blue color */
            color: #fff; /* White text color */
        }
        .proposal-info {
            margin-bottom: 20px;
        }
        .proposal-info p {
            margin: 5px 0;
        }
        .proposal-details {
            margin-top: 30px;
        }
        .proposal-details p {
            margin: 5px 0;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
        }
        .logo {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 100px; /* Adjust the width as needed */
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="logo.png" alt="Company Logo" class="logo">
        <h1>Proposal</h1>
        <div class="proposal-info">
            <p><strong>Customer:</strong> [Customer Name]</p>
            <p><strong>Proposal Date:</strong> [Proposal Date]</p>
            <p><strong>Due Date:</strong> [Due Date]</p>
        </div>
        <div class="proposal-details">
            <h2>Proposal Details</h2>
            <table>
                <thead>
                    <tr>
                        <th>Unit</th>
                        <th>Product</th>
                        <th>Unit Price</th>
                        <th>Total Price</th>
                        <th>Bulk Purchase Discount</th>
                        <th>Early Payment Discount</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Product A</td>
                        <td>$10</td>
                        <td>$10</td>
                        <td>$1</td>
                        <td>$2</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>Product B</td>
                        <td>$20</td>
                        <td>$40</td>
                        <td>$3</td>
                        <td>$5</td>
                    </tr>
                    <!-- Add more rows as needed -->
                </tbody>
            </table>
            <p>[Advertise the proposal here. Use a marketing language. Try to make the offer appealing and attractive for the customer.]</p>
            <p><strong>Delivery Date:</strong> [Delivery Date]</p>
            <p><strong>Payment Terms:</strong> [Payment Terms]</p>
        </div>
        <div class="footer">
            <p>Thank you for considering our proposal.</p>
            <p>Pistachio Electronics</p>
        </div>
    </div>
</body>
</html>
"""


customers = customer = '''
Customer ID,Customer Name,Is Current Customer,Last Proposal Date,Proposal Success Rate (%),Business Potential(Size, Profitability),Total Successful Proposals (EUR),Industry
1,Fashion Forward Inc.,Yes,2023-12-15,80,Medium,High,35000,Technology
2,XYZ Corporation,No,2023-10-20,65,High,High,25000,Finance
3,LMN Enterprises,Yes,2024-01-05,75,Medium,Medium,30000,Manufacturing
4,Smith & Sons,No,2023-11-30,45,Low,Low,15000,Retail
5,Johnson Ltd,Yes,2024-02-10,90,High,High,40000,Services
6,Miller Industries,Yes,2024-03-25,85,High,High,45000,Manufacturing
7,GreenTech Inc.,No,2023-09-18,60,Medium,Medium,20000,Technology
8,Harper & Co.,Yes,2024-04-02,70,Medium,Medium,28000,Finance
9,Jones Group,Yes,2024-02-28,75,High,High,30000,Retail
10,Brown Enterprises,No,2023-08-12,40,Low,Medium,12000,Services
11,White Innovations,Yes,2024-03-10,95,High,High,50000,Technology
12,Clark Solutions,Yes,2024-04-20,80,Medium,High,36000,Manufacturing
13,Hillcrest Industries,No,2023-07-05,50,Low,Low,18000,Finance
14,Wilson Partners,Yes,2024-02-15,85,High,High,38000,Retail
15,Anderson & Sons,Yes,2024-01-20,75,Medium,Medium,32000,Services
16,Thomas Technologies,No,2023-05-30,55,Medium,Medium,22000,Technology
17,Carter Enterprises,Yes,2023-11-05,90,High,High,40000,Manufacturing
18,Evans Group,Yes,2024-03-05,80,High,High,35000,Finance
19,Young Co.,No,2023-04-18,45,Low,Low,14000,Retail
20,Roberts Inc.,Yes,2024-04-10,75,Medium,Medium,33000,Services
21,Bennett Solutions,Yes,2024-02-28,85,High,High,38000,Technology
22,Garcia & Garcia,Yes,2023-12-10,75,Medium,High,31000,Manufacturing
23,Kelly Enterprises,Yes,2024-01-15,70,Medium,Medium,29000,Finance
24,Fisher Corporation,Yes,2024-03-20,90,High,High,42000,Retail
25,Ross Innovations,Yes,2024-02-05,80,High,High,36000,Services
26,Perez Group,Yes,2023-11-20,75,Medium,Medium,31000,Technology
27,Cooper & Co.,No,2023-03-25,50,Low,Low,16000,Manufacturing
28,Reed & Reed,Yes,2024-04-05,95,High,High,48000,Finance
29,Stewart Solutions,Yes,2024-03-10,85,High,High,38000,Retail
30,Hernandez Enterprises,No,2023-02-15,45,Low,Low,14000,Services
31,Gonzalez Inc.,Yes,2024-02-20,75,High,High,32000,Technology
32,Turner & Turner,Yes,2024-01-25,80,High,High,35000,Manufacturing
33,Diaz Group,Yes,2023-12-01,70,Medium,Medium,29000,Finance
34,Phillips & Co.,No,2022-12-10,40,Low,Low,11000,Retail
35,Scott Enterprises,Yes,2024-03-15,90,High,High,40000,Services
36,Hall & Hall,Yes,2024-04-20,85,High,High,37000,Manufacturing
37,Young Enterprises,Yes,2023-11-05,75,Medium,Medium,31000,Finance
38,Baker Group,No,2022-11-30,50,Low,Low,17000,Technology
39,Sanchez & Sons,Yes,2024-02-05,95,High,High,48000,Retail
40,King Solutions,Yes,2024-01-10,80,High,High,35000,Services
41,Rivera Corporation,No,2022-10-25,45,Low,Low,14000,Manufacturing
42,Marshall Inc.,Yes,2023-12-20,70,Medium,High,31000,Finance
43,Griffin Group,Yes,2024-03-05,85,High,High,37000,Retail
44,Hayes & Hayes,Yes,2024-04-10,90,High,High,42000,Services
45,Morgan & Morgan,Yes,2023-10-15,75,Medium,Medium,30000,Manufacturing
46,Fleming Enterprises,Yes,2024-01-25,80,High,High,35000,Finance
47,Warren Solutions,No,2022-09-20,40,Low,Low,12000,Retail
48,Scott & Scott,Yes,2024-03-20,95,High,High,48000,Services
49,Weston Inc.,Yes,2024-04-25,85,High,High,38000,Manufacturing
50,Murray Group,Yes,2023-11-10,75,Medium,Medium,32000,Finance
51,Chavez Enterprises,Yes,2024-02-15,90,High,High,42000,Retail
52,Knight & Knight,Yes,2024-01-30,80,High,High,36000,Services
53,Porter Solutions,Yes,2023-12-05,70,Medium,High,30000,Manufacturing
54,Harris Corporation,No,2022-08-10,45,Low,Low,14000,Finance
55,Watson & Watson,Yes,2024-03-10,95,High,High,48000,Retail
56,Olson Enterprises,Yes,2024-04-15,85,High,High,37000,Services
57,Fox Group,Yes,2023-10-20,75,Medium,Medium,31000,Manufacturing
58,Dunn & Dunn,No,2022-07-25,40,Low,Low,13000,Technology
59,Mills Inc.,Yes,2024-01-05,70,Medium,High,30000,Finance
60,Gibson Solutions,Yes,2024-02-10,85,High,High,37000,Retail
61,Reyes Enterprises,Yes,2024-03-25,90,High,High,43000,Services
62,Shaw Corporation,Yes,2023-09-18,75,Medium,Medium,31000,Manufacturing
63,Garza Group,Yes,2024-04-02,80,High,High,35000,Finance
64,Barnes & Barnes,Yes,2024-02-28,70,Medium,High,31000,Retail
65,Webb Solutions,No,2022-06-12,45,Low,Low,13000,Services
66,Reid & Reid,Yes,2024-03-10,95,High,High,49000,Manufacturing
67,Holland Enterprises,Yes,2024-04-20,85,High,High,38000,Finance
68,Curtis Corporation,Yes,2023-11-30,75,Medium,Medium,33000,Retail
69,Butler Group,No,2022-05-05,40,Low,Low,10000,Services
70,Simmons Inc.,Yes,2024-02-15,70,Medium,High,31000,Manufacturing
71,Hardy Solutions,Yes,2024-01-20,85,High,High,36000,Finance
72,Wong Enterprises,Yes,2024-03-05,90,High,High,43000,Retail
73,McCarthy & McCarthy,Yes,2023-09-05,75,Medium,Medium,32000,Services
74,Matthews Group,Yes,2024-04-10,80,High,High,35000,Manufacturing
75,Haynes Corporation,Yes,2024-02-01,95,High,High,48000,Finance
'''