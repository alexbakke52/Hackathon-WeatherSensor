#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include "events.h"
#include <iostream>
#include <QObject>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

MainWindow* MainWindow::getMainWindow()
{
    return this;
}

void MainWindow::on_pushButton_clicked()
{
    events myEvents;
    myEvents.precipitationPopup();
}


void MainWindow::on_pushButton_2_clicked()
{
    reader myReader;
    QObject::connect(&timer,&QTimer::timeout, doReadData);
    timer.start(1000);
}

void MainWindow::doReadData()
{
    std::cout << "Hey I'm reading data" << std::endl;
}

void MainWindow::on_pushButton_3_clicked()
{
    timer.stop();
}

