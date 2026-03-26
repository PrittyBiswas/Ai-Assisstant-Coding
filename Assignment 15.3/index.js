const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

/* ===============================
   TASK 1: FOOD ORDERING API
================================ */

let menu = [
    { id: 1, name: "Pizza", price: 200 },
    { id: 2, name: "Burger", price: 100 }
];

let orders = [];
let orderId = 1;

// GET /menu → List dishes
app.get('/menu', (req, res) => {
    res.json(menu);
});

// POST /order → Place order
app.post('/order', (req, res) => {
    const order = {
        id: orderId++,
        items: req.body.items,
        status: "Placed"
    };
    orders.push(order);
    res.json(order);
});

// GET /order/:id → Track order
app.get('/order/:id', (req, res) => {
    const order = orders.find(o => o.id == req.params.id);
    if (!order) return res.status(404).json({ error: "Order not found" });
    res.json(order);
});

// PUT /order/:id → Update order
app.put('/order/:id', (req, res) => {
    const order = orders.find(o => o.id == req.params.id);
    if (!order) return res.status(404).json({ error: "Order not found" });

    order.items = req.body.items;
    res.json(order);
});

// DELETE /order/:id → Cancel order
app.delete('/order/:id', (req, res) => {
    const index = orders.findIndex(o => o.id == req.params.id);
    if (index === -1) return res.status(404).json({ error: "Order not found" });

    const deleted = orders.splice(index, 1);
    res.json({ message: "Order cancelled", order: deleted });
});


/* ===============================
   TASK 2: EMPLOYEE PAYROLL API
================================ */

let employees = [];
let empId = 1;

// GET employees
app.get('/employees', (req, res) => {
    res.json(employees);
});

// POST employee
app.post('/employees', (req, res) => {
    const { name, salary } = req.body;

    if (!name || !salary) {
        return res.status(400).json({ error: "Invalid data" });
    }

    const emp = { id: empId++, name, salary };
    employees.push(emp);
    res.json(emp);
});

// PUT salary update
app.put('/employees/:id/salary', (req, res) => {
    const emp = employees.find(e => e.id == req.params.id);
    if (!emp) return res.status(404).json({ error: "Employee not found" });

    emp.salary = req.body.salary;
    res.json(emp);
});

// DELETE employee
app.delete('/employees/:id', (req, res) => {
    const index = employees.findIndex(e => e.id == req.params.id);
    if (index === -1) return res.status(404).json({ error: "Not found" });

    employees.splice(index, 1);
    res.json({ message: "Employee removed" });
});


/* ===============================
   TASK 3: STUDENT API
================================ */

let students = [];
let studentId = 1;

// Add student
app.post('/students', (req, res) => {
    const { name, roll, course, year } = req.body;

    const student = { id: studentId++, name, roll, course, year };
    students.push(student);

    res.json(student);
});

// Get all students
app.get('/students', (req, res) => {
    res.json(students);
});

// Update student
app.put('/students/:id', (req, res) => {
    const student = students.find(s => s.id == req.params.id);
    if (!student) return res.status(404).json({ error: "Not found" });

    Object.assign(student, req.body);
    res.json(student);
});

// Delete student
app.delete('/students/:id', (req, res) => {
    const index = students.findIndex(s => s.id == req.params.id);
    if (index === -1) return res.status(404).json({ error: "Not found" });

    students.splice(index, 1);
    res.json({ message: "Student deleted" });
});


/* ===============================
   TASK 4: WEATHER API
================================ */

const API_KEY = "YOUR_API_KEY";

// Current weather
app.get('/weather/current/:city', async (req, res) => {
    try {
        const response = await axios.get(
            `https://api.openweathermap.org/data/2.5/weather?q=${req.params.city}&appid=${API_KEY}&units=metric`
        );

        res.json({
            temperature: response.data.main.temp,
            humidity: response.data.main.humidity,
            condition: response.data.weather[0].main
        });
    } catch {
        res.status(500).json({ error: "Failed to fetch weather" });
    }
});

// Forecast
app.get('/weather/forecast/:city', async (req, res) => {
    try {
        const response = await axios.get(
            `https://api.openweathermap.org/data/2.5/forecast?q=${req.params.city}&appid=${API_KEY}&units=metric`
        );

        res.json(response.data.list);
    } catch {
        res.status(500).json({ error: "Error fetching forecast" });
    }
});


/* ===============================
   SERVER START
================================ */

app.listen(3000, () => {
    console.log("Server running on http://localhost:3000");
});