import { RouterModule } from '@angular/router';
import { Component } from '@angular/core';
import {NgForm} from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
@Component({
  selector: 'app-search',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule],
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  eventName: string = '';

  constructor(private http: HttpClient) {}

  searchEvents(searchForm: NgForm): void {
    if (searchForm.valid) {
      // Invio della richiesta POST al server sulla porta 5003
      this.http.post('http://localhost:5003/events', searchForm.value).subscribe(
        (response) => {
          console.log('Risposta dal server:', response);
          console.log('success:', response);
        },
        (error) => {
          console.error('Errore durante la richiesta:', error);
        }
      );
    }
  }
}
