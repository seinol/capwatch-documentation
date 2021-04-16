workspace "65674" "Modell für die Software CapWatch." {

    model {
        consumer = person "Konsument" "Benutzer der auf die Software CapWatch zugreift."
        store = softwareSystem "Store Auslastungs- informationssystem" "Kennt die aktuelle Auslastung eines Stores und liefert diese periodisch an CapWatch." "store"

        capWatch = softwareSystem "CapWatch" "Erlaubt es Konsumenten Informationen über die aktuelle Auslastung von Stores zu beziehen und Stores diese Informationen zu aktualisieren." {
            webApplication = container "Web Applikation" "Liefert statischen Inhalt und die CapWatch Frontend Applikation." "Alpine mit Nginx"
            frontend = container "Single-Page Applikation" "Liefert dem Konsument alle Funktionalität von CapWatch." "TypeScript und React" "website"

            backend = container "API Applikation" "Empfängt und liefert Auslastungsinformationen via JSON/HTTP API" "C#" {
                storeController = component "Store Controller" "Empfängt und liefert Informationen zu Stores inklusive Auslastungsinformationen über individuelle API Endpunkte" "C# REST Controller"
                storeRepository = component "Store Repository" "Stellt Funktionalität zum lesen und schreiben von Store Informationen zur Verfügung" "C#"
            }

            db = container "Datenbank" "Speichert Informationen über Stores und deren Auslastung" "MongoDB" "database"
        }

        consumer -> capWatch "schaut die aktuelle Auslastung von Stores an"
        consumer -> webApplication "geht auf die Homepage von CapWatch" "HTTP"
        consumer -> frontend "schaut sich die aktuelle Auslastung an"

        store -> capWatch "liefert die aktuelle Auslastung eines Stores"
        store -> backend "macht API Aufrufe an" "JSON/HTTP"
        store -> storeController "spricht einzelne APIs an" "JSON/HTTP"

        webApplication -> frontend "liefert das CapWatch Frontend an den Browser des Konsumenten"

        frontend -> backend "macht API Aufrufe an" "JSON/HTTP"
        frontend -> storeController "spricht einzelne APIs an" "JSON/HTTP"

        backend -> db "liest von und schreibt auf" "C# MongoDB driver"

        storeController -> storeRepository "benutzt"

        storeRepository -> db "liest von und schreibt auf" "C# MongoDB driver"
    }

    views {
        systemContext capWatch "SystemContext" "System Context Diagramm der Software CapWatch" {
            include *
        }

        container capWatch "CapWatchContainers" "Container Ansicht der Software CapWatch" {
            include *
        }

        component backend "BackendComponents" "Komponenten der Backend API Applikation" {
            include *
        }

        styles {
            element "Software System" {
                background #0d47a1
                color #ffffff
            }
            element "Container" {
                background #2196f3
                color #ffffff
            }
            element "website" {
                shape webbrowser
                background #2196f3
                color #ffffff
            }
            element "database" {
                shape cylinder
                background #2196f3
                color #ffffff
            }
            element "Component" {
                background #bbdefb
                color #000000
            }
            element "Person" {
                shape person
                background #212121
                color #ffffff
            }
            element "store" {
                background #9e9e9e
                color #000000
            }
        }
    }
}
