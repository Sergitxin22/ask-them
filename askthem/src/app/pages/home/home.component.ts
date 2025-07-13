import { Component, OnInit } from '@angular/core';
import { HeaderComponent } from "./components/header/header.component";
import { GroupsSectionComponent } from "./components/groups-section/groups-section.component";
import { Usuario } from '../../models/models';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [HeaderComponent, GroupsSectionComponent],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  user: Usuario;
  groups: string[] = [];

  constructor() {
    this.user = {
      id: 1,
      username: "Carlitos",
      password: "hola123",
      monedas: 653
    };
  }

  ngOnInit(): void {
    console.log(this.user);

  }
}
