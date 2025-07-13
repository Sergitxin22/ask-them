import { AsyncPipe } from '@angular/common';
import { Component, Input } from '@angular/core';
import { SvgPipe } from '../../../../pipes/svg/svg.pipe';
import { GroupCardComponent } from "../group-card/group-card.component";
import { Usuario } from '../../../../models/models';

@Component({
  selector: 'app-groups-section',
  imports: [AsyncPipe, SvgPipe, GroupCardComponent],
  templateUrl: './groups-section.component.html',
  styleUrl: './groups-section.component.css'
})
export class GroupsSectionComponent {
  @Input() user: Usuario | null = null;
  items: string[] = ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4', 'Grupo 5', 'Grupo 6', 'Grupo 7', 'Grupo 8', 'Grupo 9', 'Grupo 10'];

  constructor() { }
}
