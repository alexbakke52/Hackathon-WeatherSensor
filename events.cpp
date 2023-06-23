#include "events.h"
#include <QMessageBox>

events::events()
{

}

void events::precipitationPopup ()
{
    QMessageBox popup;
    QFont font;
    font.setBold(true);
    font.setPixelSize(48);

    popup.setFont(font);
    popup.setWindowTitle("PRECIPITATION WARNING");
    popup.setText("RAIN WARNING!");
    popup.setIcon(QMessageBox::Critical);
    popup.setStyleSheet("QLabel{min-width: 250px; min-height: 250px}");
    popup.exec();
}
